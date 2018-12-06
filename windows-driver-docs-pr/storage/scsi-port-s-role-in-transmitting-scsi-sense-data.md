---
title: SCSI Port's Role in Transmitting SCSI Sense Data
description: SCSI Port's Role in Transmitting SCSI Sense Data
ms.assetid: 27acaa0f-5b8f-43a3-9c2b-d23943114335
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SCSI Port's Role in Transmitting SCSI Sense Data


## <span id="ddk_scsi_ports_role_in_transmitting_scsi_sense_data_kg"></span><span id="DDK_SCSI_PORTS_ROLE_IN_TRANSMITTING_SCSI_SENSE_DATA_KG"></span>


The SCSI Port driver is responsible for querying a device for SCSI-2 request sense data whenever a higher-level component, such as the class driver, requests it. To request sense data, the higher-level component must provide a buffer of the length specified by the **SenseInfoBufferLength** member of the SRB to hold the request sense data pointed to by the **SenseInfoBuffer** member of the SRB. SCSI Port determines whether these two fields are defined in each SRB that it receives. If they are defined, SCSI Port furnishes SCSI-2 request sense data whenever the target controller returns a check condition in response to the SRB.

SCSI Port is also responsible for translating the request sense data into the appropriate SRB format before storing it in the buffer that is pointed to by **SenseInfoBuffer**.

When SCSI Port completes the IRP\_MJ\_SCSI IRP associated with the SRB, it must indicate that it is returning request-sense information by setting the **SrbStatus** member of the SRB to SRB\_STATUS\_AUTOSENSE\_VALID.

 

 




