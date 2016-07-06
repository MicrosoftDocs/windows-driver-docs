---
title: NFC architecture
author: windows-driver-content
description: The high-level architecture diagram of the NFC stack on Windows is shown further below. NFC UMDF drivers will implement the DDIs described in this specification.
ms.assetid: 0FA2BE92-05E1-40D1-AD1D-AE9ADF425E67
keywords: ["NFC", "near field communications", "proximity", "near field proximity", "NFP"]
---

# NFC architecture


The high-level architecture diagram of the NFC stack on Windows is shown further below. NFC UMDF drivers will implement the DDIs described in this specification.

-   [Near Field Proximity DDI](https://msdn.microsoft.com/library/windows/hardware/jj866056) – Provides publish/subscribe ability for proximity message passing, including peer to peer exchange of proximity messages and receiving and writing data from NFC tags.
-   [Secure Element DDI](https://msdn.microsoft.com/library/windows/hardware/dn905485) – Provides access to enumerate secure elements (SEs) attached to the NFC controller, allows the secure elements to be exposed to external readers and allows forwarding of events from NFCC and applets to higher layers, and also provides access to configure and manage NFC chip listen mode routing configuration. It also provides access to receive and transmit ISO/IEC 7816-4 APDUs in listen mode to a remote device.
-   [Smart Card DDI](https://msdn.microsoft.com/library/windows/hardware/dn905601) – Provides low level access for interacting with smart cards like ability to listen for card arrival/departure, allows requests to be transmitted to the smart card, and allows smart card information to be retrieved.
-   [Radio Management DDI](https://msdn.microsoft.com/library/windows/hardware/dn905577) – Provides access for the Control Panel (CPL) application to set radio states of proximity (P2P and reader/writer modes) and secure element (card emulation mode).

![](images/nfcarchitecture.png "A flowchart describing the NFC stack starting from Applications at the top, User mode services, UMDF Drivers, Kernel Mode, then Hardware at the bottom. ")

 

 
## Related topics
 [NFC device driver interface (DDI) reference](https://msdn.microsoft.com/library/windows/hardware/mt715815)  
 
------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20NFC%20architecture%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")
