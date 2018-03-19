---
title: POS events
description: POS events
ms.assetid: '1123b789-c0ee-4490-9081-79c08fc31417'
---

POS events
==========

This section describes the events that are passed from the device driver to the Point of Service (POS) API layer by using [ReadFile](http://go.microsoft.com/fwlink/p/?LinkId=314125). When an application successfully claims a device through the POS API, the runtime will maintain a continuous read operation against the device driver to receive events. The I/O is message-based. **ReadFile** needs to pass in a buffer sufficiently large enough to read in the current event. The driver retains the message until a read request with a sufficient output buffer to read the entire message is made.

## In this section


[ReleaseDeviceRequested](releasedevicerequested.md)

[StatusUpdated](statusupdated.md)
 

 





