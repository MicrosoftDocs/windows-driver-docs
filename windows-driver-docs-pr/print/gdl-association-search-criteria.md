---
title: GDL Association Search Criteria
description: GDL Association Search Criteria
ms.assetid: f591e944-a6dc-406a-a15e-7af0cc70d7f5
keywords:
- templates WDK GDL , associating templates with keywords
- keywords WDK GDL , associating templates with keywords
- templates WDK GDL , association search criteria
- association search criteria WDK GDL
- GDL WDK , searching for entries
- GDL WDK , entries
- unidentified entries WDK GDL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# GDL Association Search Criteria


Every data entry exists at the root level or as a member of a parent construct. If the entry resides at the root level, the members list that the root-level template defines is searched for the first template that qualifies to be associated with the entry. If the data entry is found within a construct, the members list of the template that is associated with the parent construct is used.

The members list is searched, starting with the most recently added element. When the members list has been searched and if the template that contains the members list has been derived from an inherited template, the search will continue with the template that is named by the \*Inherits entry and continue until the oldest template's members list has been searched.

The search will end when a template that qualifies to represent the data entry has been found. If no qualifying template has been found when the end of the list is reached, the data entry will be left without a template association; such data entries are called *unidentified entries*. All members of an unidentified data construct will also be unidentified.

 

 




