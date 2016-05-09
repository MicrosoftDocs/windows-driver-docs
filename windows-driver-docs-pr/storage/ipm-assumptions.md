---
title: IPM Assumptions
author: windows-driver-content
description: IPM Assumptions
ms.assetid: 3c8d8121-9987-43d3-b573-4ca1d26fef7d
---

# IPM Assumptions


A disk spin up operation completes within 240 seconds (4 minutes) from the time the SCSI Start Unit command is issued to the LUN.

The following SCSI commands (SRB\_FUNCTION\_EXECUTE\_SCSI operations) are expected to complete without requiring the disk to be spun up. In other words, no prior SCSI Start Unit command is required.

INQUIRY

REPORT LUNS

Miniport drivers are expected to complete all SRBs except SRB\_FUNCTION\_IO\_CONTROL, SRB\_FUNCTION\_FLUSH, and SRB\_FUNCTION\_SHUTDOWN when the LUN is in a low power state.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20IPM%20Assumptions%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


