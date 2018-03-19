---
title: PostScanJobEndStateEvent.PostScanJobEndState.FilterCompletedStatuses.FilterStatus.FilterStateReasons.FilterStateReason
description: PostScanJobEndStateEvent.PostScanJobEndState.FilterCompletedStatuses.FilterStatus.FilterStateReasons.FilterStateReason
ms.assetid: c4d894b9-1342-477d-84b5-e208cd4620fc
keywords: ["PostScanJobEndStateEvent.PostScanJobEndState.FilterCompletedStatuses.FilterStatus.FilterStateReasons.FilterStateReason"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# PostScanJobEndStateEvent.PostScanJobEndState.FilterCompletedStatuses.FilterStatus.FilterStateReasons.FilterStateReason


The **FilterStateReason** element contains a token that indicates a reason for the error state of a filter in a post-scan job.

The **FilterStateReason** element supports the following values:

<span id="InvalidArgs"></span><span id="invalidargs"></span><span id="INVALIDARGS"></span>**InvalidArgs**  
One or more of the arguments for this filter were invalid.

<span id="OutOfDiskSpace"></span><span id="outofdiskspace"></span><span id="OUTOFDISKSPACE"></span>**OutOfDiskSpace**  
There was not enough disk space available for the filter to process an image.

<span id="ServerOutOfMemory"></span><span id="serveroutofmemory"></span><span id="SERVEROUTOFMEMORY"></span>**ServerOutOfMemory**  
The server ran out of internal memory while trying to process an image.

<span id="FileShareAccessDenied"></span><span id="fileshareaccessdenied"></span><span id="FILESHAREACCESSDENIED"></span>**FileShareAccessDenied**  
The filter did not have permission to save the processed images on the destination file share.

<span id="FileShareOutOfDiskSpace"></span><span id="fileshareoutofdiskspace"></span><span id="FILESHAREOUTOFDISKSPACE"></span>**FileShareOutOfDiskSpace**  
The destination file share did not have sufficient space to store the processed images.

<span id="SharepointAccessDenied"></span><span id="sharepointaccessdenied"></span><span id="SHAREPOINTACCESSDENIED"></span>**SharepointAccessDenied**  
The filter did not have permission to save the processed image on the destination SharePoint server.

<span id="SharepointOutOfDiskSpace"></span><span id="sharepointoutofdiskspace"></span><span id="SHAREPOINTOUTOFDISKSPACE"></span>**SharepointOutOfDiskSpace**  
The destination SharePoint server did not have sufficient space to store the processed images.

<span id="InvalidSMTPServer"></span><span id="invalidsmtpserver"></span><span id="INVALIDSMTPSERVER"></span>**InvalidSMTPServer**  
The SMTP server specified in the WSD distributed scan server configuration to use for email notification could not be accessed.

<span id="UnableToSendEmail"></span><span id="unabletosendemail"></span><span id="UNABLETOSENDEMAIL"></span>**UnableToSendEmail**  
Encountered an error that prevented the filter from sending an email notification message.

<span id="UnknownError"></span><span id="unknownerror"></span><span id="UNKNOWNERROR"></span>**UnknownError**  
An unknown error occurred while the filter was processing image data.

This element has no sub-elements.

 

 





