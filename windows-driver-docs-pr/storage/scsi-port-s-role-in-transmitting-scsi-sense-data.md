---
title: SCSI Port's Role in Transmitting SCSI Sense Data
author: windows-driver-content
description: SCSI Port's Role in Transmitting SCSI Sense Data
ms.assetid: 27acaa0f-5b8f-43a3-9c2b-d23943114335
---

# SCSI Port's Role in Transmitting SCSI Sense Data


## <span id="ddk_scsi_ports_role_in_transmitting_scsi_sense_data_kg"></span><span id="DDK_SCSI_PORTS_ROLE_IN_TRANSMITTING_SCSI_SENSE_DATA_KG"></span>


The SCSI Port driver is responsible for querying a device for SCSI-2 request sense data whenever a higher-level component, such as the class driver, requests it. To request sense data, the higher-level component must provide a buffer of the length specified by the **SenseInfoBufferLength** member of the SRB to hold the request sense data pointed to by the **SenseInfoBuffer** member of the SRB. SCSI Port determines whether these two fields are defined in each SRB that it receives. If they are defined, SCSI Port furnishes SCSI-2 request sense data whenever the target controller returns a check condition in response to the SRB.

SCSI Port is also responsible for translating the request sense data into the appropriate SRB format before storing it in the buffer that is pointed to by **SenseInfoBuffer**.

When SCSI Port completes the IRP\_MJ\_SCSI IRP associated with the SRB, it must indicate that it is returning request-sense information by setting the **SrbStatus** member of the SRB to SRB\_STATUS\_AUTOSENSE\_VALID.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[storage\storage]:%20SCSI%20Port's%20Role%20in%20Transmitting%20SCSI%20Sense%20Data%20%20RELEASE:%20%285/9/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


