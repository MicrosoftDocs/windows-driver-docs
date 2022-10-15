---
title: MSFC_FibrePortNPIVMethodsEx WMI Class (Windows Drivers)
description: Learn more about the MSFC_FibrePortNPIVMethodsEx WMI Class.
ms.date: 10/14/2022
---

# MSFC\_FibrePortNPIVMethodsEx WMI Class

A NPIV WMI provider uses the **MSFC\_FibrePortNPIVMethodsEx** class to allow a management client to create virtual ports. This is particularly useful for migrating files associated with a virtual machine from one host to another.

This WMI class contains only methods and has no data blocks. Therefore, the WMI tool suite generates structures that hold parameter data for the methods that belong to this class, but it does not generate a structure that corresponds to the class itself. Included are methods to set and remove DH-CHAP authentication for virtual ports.

The MOF file syntax for each method that belongs to this class is described in the reference page for the method. The following topics describe these methods and their accompanying structures:

[**CreateVirtualPortEx**](createvirtualportex.md)

[**CreateVirtualPortExUsingDHCHAP**](createvirtualportexusingdhchap.md)

[**RemoveChapForPhysicalPort**](removechapforphysicalport.md)

[**RemoveVirtualPortEx**](removevirtualportex.md)

[**RescanVirtualPort**](rescanvirtualport.md)

[**SetChapForPhysicalPort**](setchapforphysicalport.md)
