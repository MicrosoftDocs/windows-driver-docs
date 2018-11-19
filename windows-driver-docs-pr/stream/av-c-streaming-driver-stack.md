---
title: AV/C Streaming Driver Stack
description: AV/C Streaming Driver Stack
ms.assetid: 2584c74c-ddd6-43cc-9a8c-cd7f43802c4c
keywords:
- AV/C WDK , Stream filter driver
- Stream filter driver WDK AV/C
- Avcstrm.sys streaming filter driver WDK , driver stacks
- driver stacks WDK AV/C streaming
- stacks WDK AV/C streaming
- peer driver stacks WDK AV/C streaming
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# AV/C Streaming Driver Stack





Windows loads *Avcstrm.sys* between a subunit driver's functional device object (FDO) and the corresponding physical device object (PDO) created by *Avc.sys*. *Avcstrm.sys* resides between individual subunit drivers and the function driver, *Avc.sys*. *Avcstrm.sys* is installed as a lower-level filter driver to subunit drivers in order to provide its streaming services. The interface to the streaming service provided by *Avcstrm.sys* is based on the I/O request packet (IRP) model used by the WDM architecture, with a list of supported I/O control (IOCTL) functions. *Avcstrm.sys* can service a subunit driver that is based on either the Stream class or the AVStream interfaces. The AVStream driver model is the preferred interface to use. The following diagram illustrates where *Avcstrm.sys* fits into the AV/C driver stack.

![diagram illustrating a peer av/c driver stack with the avcstrm.sys lower-filter driver](images/avcsdiag.gif)

*Avcstrm.sys* is format-aware. It must know the data format of the streaming data, such as SDDV or MPEG2TS, in order to make the proper isochronous connection between the source and the target devices. With the given format information, *Avcstrm.sys* can then interface with the AV/C subunit's driver through the 61883 protocol driver to receive or transmit data. Because *Avcstrm.sys* is format-aware, it will have to be updated to add a different format (for example, a service pack or new operating system release). Currently, SDDV and MPEG2TS formats are the only formats implemented.

In the future, *Avcstrm.sys* may be extended to:

-   Query data format

-   Perform data intersection (negotiate data format between two pins)

-   Be a clock provider

-   Get and set streaming properties

Currently, each subunit driver must implement the preceding operations.

The AV/C Streaming filter driver does not timestamp data at this time. A clock provider needs to timestamp the data as well as provide the current stream time. The subunit driver must timestamp the data if it is a clock provider.

 

 




