---
title: Synchronizing Key Exchange with Data Flow
description: Synchronizing Key Exchange with Data Flow
ms.assetid: 54abc258-d26a-4d42-a5aa-712cdae76b6d
keywords:
- DVD decoder minidrivers WDK , copyright protection
- decoder minidrivers WDK DVD , copyright protection
- copyright protection WDK DVD decoder
- key exchange WDK DVD decoder
- decryption WDK DVD decoder
- encryption WDK DVD decoder
- cryptography WDK DVD decoder
- DVD decrypters WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Synchronizing Key Exchange with Data Flow





The key exchange process may begin before all data from the previous key is processed. An example of this would be in the transition from the trailer title set into the main program title set on some movies. There is a flag in the **TypeSpecificFlags** member of the [**KSSTREAM\_HEADER**](https://msdn.microsoft.com/library/windows/hardware/ff567138) structure for each data packet. This flag is **KS\_AM\_UseNewCSSKey**, which is defined in *ksmedia.h*. It indicates that the data sample immediately following that header is the first data sample to which the new title key applies.

If the decrypter can process a new key exchange while still using the old key, the DVD decoder minidriver should process the key exchange as it receives the properties. If the decrypter must wait until all movie data requiring the previous key has been processed, then the decrypter holds the SRB for the **Set** property. The decrypter uses the [**KS\_DVDCOPY\_SET\_COPY\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567639) structure with the parameter **KS\_DVDCOPYSTATE\_INITIALIZE** or **KS\_DVDCOPYSTATE\_INITIALIZE\_TITLE** until it has received the **KS\_AM\_UseNewCSSKey** flag on all streams that are connected to it. After that, the DVD decoder minidriver processes all packets received until that point. This prevents using the incorrect key on the data.

 

 




