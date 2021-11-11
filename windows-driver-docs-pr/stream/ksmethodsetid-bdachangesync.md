---
title: KSMETHODSETID_BdaChangeSync
description: KSMETHODSETID_BdaChangeSync is the BDA change sync method set.
ms.date: 10/12/2021
ms.localizationpriority: medium
---

# KSMETHODSETID_BdaChangeSync

**KSMETHODSETID_BdaChangeSync** is the BDA change sync method set. It is used to coordinate a list of property requests on a filter and its pins and nodes.

The following methods are available:

[**KSMETHOD_BDA_START_CHANGES**](ksmethod-bda-start-changes.md)  
Resets a change list and starts keeping track of a new set of changes.

[**KSMETHOD_BDA_CHECK_CHANGES**](ksmethod-bda-check-changes.md)  
Determines whether a list of requested changes will work.

[**KSMETHOD_BDA_COMMIT_CHANGES**](ksmethod-bda-commit-changes.md)  
Commits a list of requested changes.

[**KSMETHOD_BDA_GET_CHANGE_STATE**](ksmethod-bda-get-change-state.md)  
Determines the current change state for a filter.

## Comments

This method set is implemented on filters. The network provider filter can use this method set to begin a list of changes, make the changes, then commit them all at once.
