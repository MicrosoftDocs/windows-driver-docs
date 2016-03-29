---
title: GDL Association Search Criteria
description: GDL Association Search Criteria
ms.assetid: f591e944-a6dc-406a-a15e-7af0cc70d7f5
keywords: ["templates WDK GDL , associating templates with keywords", "keywords WDK GDL , associating templates with keywords", "templates WDK GDL , association search criteria", "association search criteria WDK GDL", "GDL WDK , searching for entries", "GDL WDK , entries", "unidentified entries WDK GDL"]
---

# GDL Association Search Criteria


Every data entry exists at the root level or as a member of a parent construct. If the entry resides at the root level, the members list that the root-level template defines is searched for the first template that qualifies to be associated with the entry. If the data entry is found within a construct, the members list of the template that is associated with the parent construct is used.

The members list is searched, starting with the most recently added element. When the members list has been searched and if the template that contains the members list has been derived from an inherited template, the search will continue with the template that is named by the \*Inherits entry and continue until the oldest template's members list has been searched.

The search will end when a template that qualifies to represent the data entry has been found. If no qualifying template has been found when the end of the list is reached, the data entry will be left without a template association; such data entries are called *unidentified entries*. All members of an unidentified data construct will also be unidentified.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20GDL%20Association%20Search%20Criteria%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




