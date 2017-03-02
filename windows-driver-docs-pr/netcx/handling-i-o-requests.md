---
title: Handling I/O Requests
---

# Handling I/O Requests

Most PCI NICs will operate at this tier.  netadapterpacket.h

	· NetRingBufferGetPacketAtIndex
	· NetRingBufferGetNextPacket
	· NetRingBufferAdvanceNextPacket
	· NetRingBufferReturnCompletedPacketsThroughIndex
	· NetRingBufferReturnCompletedPackets

