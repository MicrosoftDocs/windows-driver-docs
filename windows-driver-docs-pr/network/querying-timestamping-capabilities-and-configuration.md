---
title: Querying timestamping capabilities and configuration
description: Overlying drivers can issue the following OID query requests to obtain hardware and software timestamping information.
ms.date: 01/31/2021
ms.localizationpriority: medium
---

# Querying timestamping capabilities and configuration

Once the miniport driver is initialized, overlying drivers and applications can issue the following OID query requests to obtain hardware and software timestamping information.

* [OID_TIMESTAMP_CAPABILITY](oid-timestamp-capability.md).
An overlying driver issues an object identifier (OID) query request of OID_TIMESTAMP_CAPABILITY to obtain the hardware timestamping capabilities of the NIC and software timestamping capabilities of the miniport driver.

* [OID_TIMESTAMP_CURRENT_CONFIG](oid-timestamp-current-config.md).
An overlying driver issues an OID query request of OID_TIMESTAMP_CURRENT_CONFIG to obtain the current timestamping configuration of the NIC.

* [OID_TIMESTAMP_GET_CROSSTIMESTAMP](oid-timestamp-get-crosstimestamp.md).
An overlying driver issues an OID query request of OID_TIMESTAMP_GET_CROSSTIMESTAMP to obtain the cross timestamp from the NIC hardware. Precision Time Protocol (PTP) version 2 applications use the information provided in this OID to establish a relation between the NIC’s hardware clock and a system clock. 


NDIS handles the OID_TIMESTAMP_CAPABILITY and OID_TIMESTAMP_GET_CROSSTIMESTAMP OIDs based on the information that the miniport driver reported when it registered the timestamping capabilities and current configuration to the operating system. 

The miniport driver completes the OID_TIMESTAMP_GET_CROSSTIMESTAMP OID. The miniport must support this OID if it sets the **CrossTimestamp** field to **TRUE** in the [**NDIS_TIMESTAMP_CAPABILITIES**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_timestamp_capabilities) structure as part of the current configuration. 

For more information on how the miniport driver reports the  timestamping capabilities, see [Reporting timestamping capabilities and current configuration](reporting-timestamping-capabilities.md).
