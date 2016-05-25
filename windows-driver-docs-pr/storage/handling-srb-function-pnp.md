---
title: Handling SRB\_FUNCTION\_PNP
author: windows-driver-content
description: Handling SRB\_FUNCTION\_PNP
ms.assetid: 25490320-8d6b-4c5a-a585-4f628ea72393
---

# Handling SRB\_FUNCTION\_PNP


The port driver sends SCSI\_PNP\_REQUEST\_BLOCK requests to a miniport driver to notify the miniport driver of Windows Plug and Play (PnP) events that affect storage devices that are connected to the adapter.

These requests merely represent notifications that PnP events are occurring and do not require any action by the miniport driver. A miniport driver can do real work within the context of a PnP request (such as disabling its hardware, for example) but is not required to do so.

If the function member of an SRB is set to SRB\_FUNCTION\_PNP, the SRB is a structure of type SCSI\_PNP\_REQUEST\_BLOCK.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20Handling%20SRB_FUNCTION_PNP%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


