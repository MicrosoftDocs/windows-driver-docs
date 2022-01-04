---
title: GUID_NDIS_ENUMERATE_ADAPTERS_EX
description: This topic describes the GUID_NDIS_ENUMERATE_ADAPTERS_EX GUID for the NDIS WMI interface.
keywords:
- GUID_NDIS_ENUMERATE_ADAPTERS_EX, WDK GUID_NDIS_ENUMERATE_ADAPTERS_EX network drivers
ms.date: 11/22/2017
---

# GUID_NDIS_ENUMERATE_ADAPTERS_EX

WMI clients can use the GUID_NDIS_ENUMERATE_ADAPTERS_EX GUID to obtain an enumeration of all of the miniport adapters on the computer. This WMI GUID is supported in NDIS 6.0 and later versions. Because NDIS tracks all of the loaded miniport adapters, NDIS does not query miniport drivers for this information.

WMI clients can use this GUID to find a device name and the associated value in the **NetLuid** member of the [NDIS_WMI_ENUM_ADAPTER](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_wmi_enum_adapter) structure. WMI clients can use the **NetLuid** value of the adapter in subsequent GUID requests.

The data buffer that NDIS returns with the GUID contains array of NDIS_WMI_ENUM_ADAPTER structures.
