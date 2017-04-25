---
title: Porting from ScsiPort to StorPort
author: windows-driver-content
description: Porting from ScsiPort to StorPort
ms.assetid: 2a14051d-dc23-4420-a3e5-0827b16b1e42
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Porting from ScsiPort to StorPort


The following is a summary of the porting activities that were necessary in order to port the sample code from a Scsiport-based miniport driver to a Storport-based miniport driver:

-   Remove all NextRequest and NextLuRequest calls

-   Rename all ScsiPortXxx calls to StorPortXxx

-   Add BuildIo routine (moved about 75% of code from StartIo)

-   Convert driver to full-duplex operation

-   Add queue management routines (error handling, adapter restart)

-   Add LUN and target reset support

-   Add code to assign queue tags internally (hardware limitation)

-   Add synchronization routines for bus reset and full adapter restart

-   Add support for SRB\_FUNCTION\_POWER (adapter shutdown through SRB)

-   Add StorPortSetDeviceQueueDepth call -- LUN queue depth set to 31

 

 


--------------------


