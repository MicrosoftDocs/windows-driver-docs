---
title: Graphics measures
description: Graphics measures filter out benign initialization errors during graphics driver flighting
ms.topic: article
ms.date: 05/20/2019
ms.localizationpriority: medium
---

# Graphics measures

The [Windows Display Driver Model](../display/roadmap-for-developing-drivers-for-the-windows-vista-display-driver-mo.md)  requires hardware vendors to submit a paired user-mode display driver and kernel-mode display driver. The user-mode display driver runs in a protected space, therefore any crashes in the driver’s binary will not crash the machine. In contrast, the kernel-mode driver has more access to machine functions and can crash the machine when erring. Together these drivers translate binary information from the OS and applications into human-readable visuals for the user. As the graphics and audio components often interact, these drivers are also assessed with [Audio measures](audio-measures.md).

Furthermore, some graphics measures count the number of user-mode crashes in applications and count the usage time of those applications. The measures then normalize the usage time to years, which Microsoft uses to calculate the number of expected crashes a user would experience if they used the application for a year.

Graphics drivers light up a breadth of scenarios, which cannot all be covered with only the flight population. Therefore, some measures have **Ecosystem Audiences** to collect more data and reduce sampling noise, increasing statistical significance. Some of these Ecosystem measures have measure counterparts with **Standard Audiences**.