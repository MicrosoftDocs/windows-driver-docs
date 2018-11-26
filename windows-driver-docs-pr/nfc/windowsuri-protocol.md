---
title: WindowsUri protocol
description: WindowsUri protocol
ms.assetid: 79589ECE-9DF9-40C8-897D-95B432C4C9C8
keywords:
- NFC
- near field communications
- proximity
- near field proximity
- NFP
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WindowsUri protocol


The “WindowsUri” protocol is a means of abstracting a subscription for a simple URI string. Windows will subscribe to this type in order to register with the driver that Windows is interested in receiving URIs that the user may be interested in launching.

### Required Actions

-   The driver MUST return the URI string as a NULL-terminated UTF-16LE encoded string for “WindowsUri” subscribers.
-   The driver MUST treat the input payload of “WindowsUri” publications as a UTF-16LE encoded string. The driver MUST safely accept either NULL-terminated or NON-NULL-terminated inputs.
-   If the proximity technology is advertised as NFC, then the driver MUST treat subscriptions for the “WindowsUri” Type as equivalent to a subscription for the URI payload within an “NDEF:wkt.U” or “NDEF:wkt.Sp” message.
    -   The driver MUST also match a “WindowsUri” subscription with the URI payload within an “NDEF:wkt.Sp” message. All subscriptions to “NDEF:wkt.Sp” MUST be filled with the full payload of a “NDEF:wkt.Sp” message. If the NDEF message contains both a smart poster and a non-nested URI record, the URI record must be ignored.
    -   The driver MUST return only the URI string PAYLOAD of this message to subscribers of this type. The driver MUST NOT return the full NDEF message to subscribers of this type.
-   If the proximity technology is advertised as NFC, then the driver MUST encapsulate the payload of each “WindowsUri” publication within NDEF messages as specified in \[NFC URI\].
-   The provider MAY support other compatible schemes as well.

## Publications for “WindowsUri:WriteTag”


This is a special type of WindowsUri publication that allows a URI to be written to any writeable tag.

### Required Actions

-   The common “\*:WriteTag” requirements described elsewhere apply.
-   The above “WindowsUri” publication requirements also apply to “WindowsUri:WriteTag” publications.

 

 
## Related topics
[NFC device driver interface (DDI) overview](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
[Near field proximity DDI reference](https://msdn.microsoft.com/library/windows/hardware/jj866056)  

