from threading import Thread;
import Messages;
import time;
import re;

class EventParser(Thread):
	def __init__(self, eventQueue):
		Thread.__init__(self);
		self.eventQueue = eventQueue;

		self.eventPattern = re.compile("^\((\w+)\)(.*)$");
		self.propertySourcePattern = re.compile("(\w+)_(\d+)");

	def run(self):
		print "Generating event";

		f = open('game.txt', 'r');
		ln = 0
		for line in f:
			match = self.eventPattern.match(line);

			ln = ln + 1
			if (match):
				groups = match.groups();

				if (groups):
					eventSource = groups[0];
					data = groups[1];

					if (eventSource == "Update"):
						propertyAndValues = data.split(",");

						i = 0;
						while i < len(propertyAndValues):
							propertyName = propertyAndValues[i];
							propertyValue = propertyAndValues[i + 1];
							propertySource = -1;
							i = i + 2

							propertyMatch = self.propertySourcePattern.match(propertyName);

							if (propertyMatch):
								propertyGroups = propertyMatch.groups();
								propertyName = propertyGroups[0];
								propertySource = propertyGroups[1];

							self.eventQueue.put(Messages.PropertyChangeMessage(eventSource, propertyName, propertySource, propertyValue));
					else:
						pass

		
