---
title: Mapping PTP Objects to WIA Items
description: Mapping PTP Objects to WIA Items
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Mapping PTP Objects to WIA Items





A WIA item is created for each PTP object present on a device. The driver displays the objects in the same hierarchy as they were reported in. For example, if all of the objects are reported under a folder named "XYZ", the pictures are displayed in Explorer under a folder named "XYZ".

One exception to this rule is for devices that report their FilesystemType as DCF in the StorageInfo dataset. In that case, the top level folder is called "DCIM" (if it exists), and the next level of folders down is hidden by the Microsoft PTP class WIA minidriver. All of the objects in the subfolders are promoted to the top level. File name extensions (for example, .JPG) are stripped from the object names before they are sent to WIA.

 

 




