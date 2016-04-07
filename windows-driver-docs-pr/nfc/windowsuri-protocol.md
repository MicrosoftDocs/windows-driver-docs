---
title: WindowsUri protocol
author: windows-driver-content
description: WindowsUri protocol
ms.assetid: 79589ECE-9DF9-40C8-897D-95B432C4C9C8
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
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

## <a href="" id="publications-for--windowsuri-writetag-"></a>Publications for “WindowsUri:WriteTag”


This is a special type of WindowsUri publication that allows a URI to be written to any writeable tag.

### Required Actions

-   The common “\*:WriteTag” requirements described elsewhere apply.
-   The above “WindowsUri” publication requirements also apply to “WindowsUri:WriteTag” publications.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20WindowsUri%20protocol%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




