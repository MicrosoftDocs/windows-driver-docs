---
title: Film Scanner Architecture
description: Film Scanner Architecture
ms.assetid: fe3a2c23-a520-4701-8178-02f50ac08767
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Film Scanner Architecture





Scanner devices that support slide or transparency scanning units should implement a film scanner item in their WIA item tree. This WIA item represents a programmable data source. It produces an image or images from film that is placed on the scanner's film scanning surface when a data transfer is requested from this item. The film scanner item should be located directly off the WIA root item and should contain one or more child items (called frames). *Frames* are film items that represent individual selection areas and the location of the selection area on the film scanning surface. The WIA driver determines whether these selections can be added, deleted, resized, or even relocated by setting the valid values of the extent settings.

The following topics describe the two types of film scanners:

[Flatbed Scanners That Support Film Scanning](flatbed-scanners-that-support-film-scanning.md)

[Dedicated Film Scanners](dedicated-film-scanners.md)

 

 




