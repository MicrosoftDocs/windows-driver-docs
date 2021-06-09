---
title: Introduction to Changer Drivers
description: Changer Drivers
keywords:
- changer drivers WDK storage
- storage changer drivers WDK
- storage drivers WDK , changer drivers
- changer drivers WDK storage , about changer drivers
- storage changer drivers WDK , about changer drivers
- autoloaders WDK storage
- autochangers WDK storage
- jukebox WDK storage
ms.date: 12/15/2019
ms.localizationpriority: medium
---

# Introduction to Changer Drivers

A changer driver controls the elements of a media library, or *changer* (sometimes called an *autoloader*, *autochanger*, or *jukebox*). In NT-based operating systems, a driver for a changer consists of the following:

- A system-supplied changer class driver provided as a library, *mcd.lib*, that provides functionality common to all changer drivers

- A device-specific miniclass driver, statically linked to *mcd.lib*, that provides routines called by the changer class driver to support a particular type of changer

This section describes the Windows changer driver model, and provides details for writing a new changer miniclass driver.
