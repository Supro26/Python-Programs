from scapy.all import sniff, IP, TCP # Scapy is a networking library that allows us to perform network and network-related operations using Python.
from collections import defaultdict
import threading
import queue
class PacketCapture:
    def __init__(self):
        self.packet_queue = queue.Queue()
        self.stop_capture = threading.Event()

    def packet_callback(self, packet):
        if IP in packet and TCP in packet:
            self.packet_queue.put(packet)

    def start_capture(self, interface="lo"):
        def capture_thread():
            sniff(iface=interface,
                  prn=self.packet_callback,
                  store=0,
                  stop_filter=lambda _: self.stop_capture.is_set())

        self.capture_thread = threading.Thread(target=capture_thread)
        self.capture_thread.start()

    def stop(self):
        self.stop_capture.set()
        self.capture_thread.join()
    
    #Line-by-line explanation
#from scapy.all import sniff, IP, TCP

#scapy is a Python library for packet manipulation and capture. It can build, send, receive, dissect, and display network packets.

#sniff — function that captures packets from an interface (or from a pcap file). It’s the core capture routine you’re using.

#IP, TCP — Scapy “layer” classes. You use them to ask “does this packet contain an IP layer?” or to access fields like packet[IP].src.

#import threading

#Python standard library for creating threads and synchronization primitives.

#You use threading.Thread to run the packet capture loop in the background.

#threading.Event is a simple boolean flag that can be set from one thread and read by other threads — great for signalling stop conditions.

#import queue

#Provides thread-safe queue implementations (FIFO). queue.Queue() is safe to use from multiple threads: one thread puts items, another thread gets them.

#Useful for decoupling capture (producer) from analysis (consumer).

#import time

#Simple standard library module often used for sleeping, timestamps, etc. (not used in your snippet but commonly paired with capture loops).

#class PacketCapture:

#Defines a new class (object blueprint) named PacketCapture. Instances of this class encapsulate capture state (queue, event, thread).

#ef __init__(self):

#Constructor — called when you create PacketCapture().

#self.packet_queue = queue.Queue()

#Creates a Queue instance.

#Purpose: captured packets are put into this queue by the capture thread. Another thread (analyzer) can get() packets from here to process them.

#Behavior: get() blocks by default (waits until an item is available), put() never blocks unless you set maxsize and it’s full.

#self.stop_capture = threading.Event()

#Creates an Event object initially in the unset state (False).

#Another thread can call self.stop_capture.set() to mark it True; threads can check is_set() to decide to stop.

#Good for safe termination across threads.

#def packet_callback(self, packet):

#This is a function passed to sniff() as prn=... (a callback executed for each received packet).

#packet is a Scapy Packet object.

#if IP in packet and TCP in packet:

#Checks whether the captured packet contains both an IP layer and a TCP layer.

#IP in packet uses Scapy’s layer membership test.

#If that condition is true, it means this packet is an IP packet carrying TCP.

#self.packet_queue.put(packet)

#Pushes the packet object into the queue for later processing.

#put() is thread-safe. If you want to avoid the producer blocking when the queue is full, you can set maxsize for the queue or use put_nowait() and handle queue.Full.

#def start_capture(self, interface="eth0"):

#Public method to start background capture on the named interface. Default interface is "eth0" (common in Linux VMs but may differ on your machine — e.g., wlan0, enp3s0, lo).

#def capture_thread():

#Inner function that will run inside a Python thread. Encapsulates the sniff call.

#sniff(iface=interface, prn=self.packet_callback, store=0, stop_filter=lambda _: self.stop_capture.is_set())

#sniff(...) arguments:

#iface=interface — which network interface to listen on.

#prn=self.packet_callback — call this function for every captured packet.

#store=0 — tells Scapy not to keep packets in memory internally (prevents Scapy from storing all packets and using lots of memory). We push to the queue instead.

#stop_filter=lambda _: self.stop_capture.is_set() — after each packet, Scapy calls stop_filter(packet). If it returns True, sniffing stops. Here stop_filter returns True when the event has been set (i.e., stop() was called).

#Note: stop_filter is evaluated only when a packet arrives — if traffic is silent, sniff keeps waiting. To ensure timely stop you may also call sniff(timeout=...) or run a separate mechanism.

#self.capture_thread = threading.Thread(target=capture_thread)

#Creates a Thread object that will run the capture_thread() function.

#self.capture_thread.start()

#Starts the thread; it begins execution concurrently with the main thread.

#def stop(self):

#Public method to stop capture and wait for the thread to finish.

#self.stop_capture.set()

#Sets the threading Event flag to True. The stop_filter lambda will read is_set() as True and cause sniff() to stop at the next processed packet.

#self.capture_thread.join()

#Waits (blocks) until the capture thread exits. This makes shutdown orderly (no zombie threads). If the thread never stops (e.g., no more packets arrive so stop_filter never runs), join() will block indefinitely — more on that in tips below.