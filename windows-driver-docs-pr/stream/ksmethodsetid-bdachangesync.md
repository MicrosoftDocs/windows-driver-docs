---
title: KSMETHODSETID\_BdaChangeSync
description: KSMETHODSETID\_BdaChangeSync
ms.assetid: 260b227d-0d49-4efa-8f8c-4c66886cf9f6
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# KSMETHODSETID\_BdaChangeSync


## <span id="ddk_ksmethodsetid_bdachangesync_ks"></span><span id="DDK_KSMETHODSETID_BDACHANGESYNC_KS"></span>


KSMETHODSETID\_BdaChangeSync is the BDA change sync method set. It is used to coordinate a list of property requests on a filter and its pins and nodes.

The following methods are available:

<span id="KSMETHOD_BDA_START_CHANGES"></span><span id="ksmethod_bda_start_changes"></span>[**KSMETHOD\_BDA\_START\_CHANGES**](ksmethod-bda-start-changes.md)  
Resets a change list and starts keeping track of a new set of changes.

<span id="KSMETHOD_BDA_CHECK_CHANGES"></span><span id="ksmethod_bda_check_changes"></span>[**KSMETHOD\_BDA\_CHECK\_CHANGES**](ksmethod-bda-check-changes.md)  
Determines whether a list of requested changes will work.

<span id="KSMETHOD_BDA_COMMIT_CHANGES"></span><span id="ksmethod_bda_commit_changes"></span>[**KSMETHOD\_BDA\_COMMIT\_CHANGES**](ksmethod-bda-commit-changes.md)  
Commits a list of requested changes.

<span id="KSMETHOD_BDA_GET_CHANGE_STATE"></span><span id="ksmethod_bda_get_change_state"></span>[**KSMETHOD\_BDA\_GET\_CHANGE\_STATE**](ksmethod-bda-get-change-state.md)  
Determines the current change state for a filter.

### Comments

This method set is implemented on filters. The network provider filter can use this method set to begin a list of changes, make the changes, then commit them all at once.

 

 





