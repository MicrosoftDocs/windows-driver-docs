---
title: NFCEE discovery sequence
ms.assetid: F6894EFD-4140-490B-B0BB-1A9BDA4DCECE
description: 
---

# NFCEE discovery sequence


Due to the limitations of the NCI 1.0 specification, chipset manufacturers have different implementations of NFCEE management. To support these varied implementations, the NFC CX provides two modes of operation:

-   **Standard NCI Mode** – In this mode, NFC CX allows the NFCC to report a single HCI network for all the NFCEEs. There isn’t a separate NFCEE\_DISCOVER\_NTF for the other NFCEEs. NFC CX, however, limits to support a single NFCEE in this configuration. An extension to this mode, if the NFCC reports a HCI network per NFCEE, the NFC CX will pick the first and discard the rest.

-   **Non-standard NCI Mode** – In this mode, NFC CX allows the NFCC to report a single HCI network for all the NFCEEs. Also, it reports the child NFCEEs on the network separately in its NFCEE\_DISCOVER\_NTF. However, the NFC CX has two additional requirements to support this configuration. The number of NFCEEs reported in the NFCEE\_DISCOVER\_RSP much include the child NFCEEs . Also, the NFCEEIDs of the child NFCCs must match the HCI Host IDs (HCI standard requires UICC Host ID to be 0x2).

Most implementations of NFCCs in this configuration report only the HCI network NFCEEID in its NFCEE\_DISCOVER\_RSP. However, since the NFC CX doesn’t know the actual number, its is unable to determine when the discovery process completes. NFC client drivers usually have a proprietary mechanism to know the additional NFCEEs that will be reporting. Therefore, NFC client driver can in its transport handling implement a small workaround to additional the additional NFCEEs in the response to satisfy this requirement.

![non-standard nci nfcee discovery sequence](images/nonstandardnci-nfceediscoverysequence.png)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnfpdrivers\nfpdrivers%5D:%20NFCEE%20discovery%20sequence%20%20RELEASE:%20%284/5/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




