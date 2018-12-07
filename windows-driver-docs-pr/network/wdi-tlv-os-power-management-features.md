---
title: WDI_TLV_OS_POWER_MANAGEMENT_FEATURES
description: WDI_TLV_OS_POWER_MANAGEMENT_FEATURES is a TLV that contains flags for OS power management features.
ms.assetid: 4F104956-1B26-47DF-A58F-53C24B75DB77
ms.date: 03/30/2018
keywords:
 - WDI_TLV_OS_POWER_MANAGEMENT_FEATURES Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI_TLV_OS_POWER_MANAGEMENT_FEATURES

WDI_TLV_OS_POWER_MANAGEMENT_FEATURES is a TLV that contains flags for OS power management features. This enables IHVs to indicate to the OS that they support an advanced power management feature called Nic Auto Power Saver (NAPS). NAPS permits the wireless adapter to enter *DX* in situations where network activity is idle.

## TLV Type

0x144

## Length


The size (in bytes) of the following values.

## Values

| Type | Description |
| --- | --- |
| [**WDI_OS_POWER_MANAGEMENT_FLAGS**](https://docs.microsoft.com/windows-hardware/drivers/ddi/content/wditypes/ne-wditypes-_wdi_os_power_management_flags) | A bitwise OR of **WDI_OS_POWER_MANAGEMENT_FLAGS** values that defines supported NAPS enablement scenarios. |
 

## Requirements

| | |
| --- | --- |
| Minimum supported client | Windows 10, version 1803 |
| Minimum supported server | Windows Server 2016 |
| Header | Wditypes.hpp |
