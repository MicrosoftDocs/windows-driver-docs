---
title: Plug and Play and Power Management
description: Plug and Play and Power Management
ms.date: 04/20/2017
---

# Plug and Play and Power Management


The LsiU3AdapterControl routine allows for special adapter control routines to be implemented without changing its HW\_INITIALIZATION\_DATA structure. It contains support for the StopAdapter and ScsiRestartAdapter ControlTypes, which replace the HwFindAdapter and HwInitialize routines for adapters going through a power management cycle. In addition, the LsiU3StartIo routine adds handling of SRBs with function code SRB\_FUNCTION\_POWER for HBA shutdown.

 

 




