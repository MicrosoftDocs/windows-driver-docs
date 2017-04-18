---
title: Synchronizing Key Exchange with Data Flow
author: windows-driver-content
description: Synchronizing Key Exchange with Data Flow
ms.assetid: 54abc258-d26a-4d42-a5aa-712cdae76b6d
keywords: ["DVD decoder minidrivers WDK , copyright protection", "decoder minidrivers WDK DVD , copyright protection", "copyright protection WDK DVD decoder", "key exchange WDK DVD decoder", "decryption WDK DVD decoder", "encryption WDK DVD decoder", "cryptography WDK DVD decoder", "DVD decrypters WDK"]
---

# Synchronizing Key Exchange with Data Flow


## <a href="" id="ddk-synchronizing-key-exchange-with-data-flow-ksg"></a>


The key exchange process may begin before all data from the previous key is processed. An example of this would be in the transition from the trailer title set into the main program title set on some movies. There is a flag in the **TypeSpecificFlags** member of the [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structure for each data packet. This flag is **KS\_AM\_UseNewCSSKey**, which is defined in *ksmedia.h*. It indicates that the data sample immediately following that header is the first data sample to which the new title key applies.

If the decrypter can process a new key exchange while still using the old key, the DVD decoder minidriver should process the key exchange as it receives the properties. If the decrypter must wait until all movie data requiring the previous key has been processed, then the decrypter holds the SRB for the **Set** property. The decrypter uses the [**KS\_DVDCOPY\_SET\_COPY\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567639) structure with the parameter **KS\_DVDCOPYSTATE\_INITIALIZE** or **KS\_DVDCOPYSTATE\_INITIALIZE\_TITLE** until it has received the **KS\_AM\_UseNewCSSKey** flag on all streams that are connected to it. After that, the DVD decoder minidriver processes all packets received until that point. This prevents using the incorrect key on the data.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Synchronizing%20Key%20Exchange%20with%20Data%20Flow%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


