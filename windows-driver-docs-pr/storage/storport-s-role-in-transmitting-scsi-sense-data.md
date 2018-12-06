---
title: Storport's Role in Transmitting SCSI Sense Data
description: Storport's Role in Transmitting SCSI Sense Data
ms.assetid: 18f2f4e0-f49b-4026-b18f-26b413f05970
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Storport's Role in Transmitting SCSI Sense Data


The Storport driver is responsible for querying a device for SCSI-3 request sense data whenever a higher-level component, such as the class driver, requests it. To request sense data, the higher-level component must provide a buffer of the length specified by the **SenseInfoBufferLength** member of the SRB to hold the request sense data pointed to by the **SenseInfoBuffer** member of the SRB. Storport determines whether these two fields are defined in each SRB that it receives. If they are defined, Storport furnishes SCSI-3 request sense data whenever the target controller returns a check condition in response to the SRB.

Storport is also responsible for translating the request sense data into the appropriate SRB format before storing it in the buffer that is pointed to by **SenseInfoBuffer**.

When Storport completes the IRP\_MJ\_SCSI IRP associated with the SRB, it must indicate that it is returning request-sense information by logical-ORing the SRB\_STATUS\_AUTOSENSE\_VALID flag in with the **SrbStatus** member of the SRB.

 

 




