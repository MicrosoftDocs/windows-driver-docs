---
title: KSMETHODSETID\_BdaChangeSync
description: KSMETHODSETID\_BdaChangeSync
ms.assetid: 260b227d-0d49-4efa-8f8c-4c66886cf9f6
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

### <span id="comments"></span><span id="COMMENTS"></span>Comments

This method set is implemented on filters. The network provider filter can use this method set to begin a list of changes, make the changes, then commit them all at once.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20KSMETHODSETID_BdaChangeSync%20%20RELEASE:%20%2811/22/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




