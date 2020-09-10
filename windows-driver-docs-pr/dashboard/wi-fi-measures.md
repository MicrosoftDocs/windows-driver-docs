---
title: Wi-Fi measures
description: Wi-Fi measures filter out benign initialization errors during Bluetooth driver flighting
ms.topic: article
ms.date: 05/20/2019
ms.localizationpriority: medium
---

# Wi-Fi measures

## Description

Microsoft provides WLAN device manufactures with the WLAN device driver interface (WDI). A WDI-compliant driver enables manufactures to develop a universal driver that is functional on device platforms, improves the quality of a WLAN driver, and reduces the complexity of the driver package. A machine can use a WDI compliant driver so its Wi-Fi component and Windows OS can communicate and enable wireless connection for the end user. For more info about WDI driver development, see [WLAN Universal Windows driver model](../network/wifi-universal-driver-model.md).

Wi-Fi measures filter out events based on the machine’s signal quality, and some will filter out the worst 5% of Wi-fi connections. This reduces noise in quality assessment. 
