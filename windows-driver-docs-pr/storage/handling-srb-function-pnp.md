---
title: Handling SRB_FUNCTION_PNP
description: Handling SRB_FUNCTION_PNP
ms.assetid: 25490320-8d6b-4c5a-a585-4f628ea72393
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Handling SRB\_FUNCTION\_PNP


The port driver sends SCSI\_PNP\_REQUEST\_BLOCK requests to a miniport driver to notify the miniport driver of Windows Plug and Play (PnP) events that affect storage devices that are connected to the adapter.

These requests merely represent notifications that PnP events are occurring and do not require any action by the miniport driver. A miniport driver can do real work within the context of a PnP request (such as disabling its hardware, for example) but is not required to do so.

If the function member of an SRB is set to SRB\_FUNCTION\_PNP, the SRB is a structure of type SCSI\_PNP\_REQUEST\_BLOCK.

 

 




