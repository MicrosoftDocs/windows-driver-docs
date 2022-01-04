---
title: POS events
description: Describes the events that are passed from the device driver to the Point of Service (POS) API layer by using ReadFile.
ms.date: 09/07/2018
---

# POS events

This section describes the events that are passed from the device driver to the Point of Service (POS) API layer by using [ReadFile](/windows/win32/api/fileapi/nf-fileapi-readfile). When an application successfully claims a device through the POS API, the runtime will maintain a continuous read operation against the device driver to receive events. The I/O is message-based. **ReadFile** needs to pass in a buffer sufficiently large enough to read in the current event. The driver retains the message until a read request with a sufficient output buffer to read the entire message is made.

## In this section

[ReleaseDeviceRequested](releasedevicerequested.md)

[StatusUpdated](statusupdated.md)
