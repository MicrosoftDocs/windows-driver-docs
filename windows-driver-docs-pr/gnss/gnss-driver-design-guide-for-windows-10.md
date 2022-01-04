---
title: Global Navigation Satellite System (GNSS) driver design guide for Windows 10
description: Describes design requirements and architecture of the Universal Windows UMDF 2.0 driver for Global Navigation Satellite System (GNSS) for the converged Windows location stack in Windows 10.
ms.date: 08/24/2021
---

# Global Navigation Satellite System (GNSS) driver design guide for Windows 10

This guide describes the design and architecture of the Universal Windows driver for GNSS (UMDF 2.0) for the converged Windows Location stack in Windows 10.

## In this section

| Topic | Description |
|--|--|
| [GNSS driver overview](gnss-driver-overview.md) | Use the GNSS driver design guide to learn how to implement the **DeviceIoControl** APIs with the GNSS driver so that a high level operating system component (HLOS) like the GNSS adapter can access the desired GNSS functionality. |
| [GNSS driver requirements](gnss-driver-requirements.md) | Describes requirements, assumptions, and constraints to consider when developing a GNSS driver for Windows 10. |
| [GNSS driver architecture](gnss-driver-architecture.md) | Provides an overview of GNSS UMDF 2.0 driver architecture, I/O considerations, and discusses several types of tracking and fix sessions. |
| [GNSS driver design](gnss-driver-design.md) | Discusses design principles to consider when developing a GNSS driver for Windows 10 including data structures, error reporting, and driver versioning. |
