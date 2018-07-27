---
title: PostScanJobStatusEvent.JobStatus.JobStateReasons.JobStateReason
description: PostScanJobStatusEvent.JobStatus.JobStateReasons.JobStateReason
ms.assetid: f10f7f9a-d052-4664-9f14-96699799afbf
keywords: ["PostScanJobStatusEvent.JobStatus.JobStateReasons.JobStateReason"]
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# PostScanJobStatusEvent.JobStatus.JobStateReasons.JobStateReason


The **JobStateReason** element contains a token that indicates a reason for the status of a post-scan job.

The **JobStateReason** element supports the following values:

<span id="None"></span><span id="none"></span><span id="NONE"></span>**None**  
No additional information is available about the status of the post-scan job.

<span id="NoValidPostScanInstructionsFound"></span><span id="novalidpostscaninstructionsfound"></span><span id="NOVALIDPOSTSCANINSTRUCTIONSFOUND"></span>**NoValidPostScanInstructionsFound**  
The [CreatePostScanJobRequest](createpostscanjobrequest.md) message contained an invalid scan processing instruction.

<span id="CreatePostScanJobFailed"></span><span id="createpostscanjobfailed"></span><span id="CREATEPOSTSCANJOBFAILED"></span>**CreatePostScanJobFailed**  
Failed to create a post-scan job in response to a [CreatePostScanJobRequest](createpostscanjobrequest.md) message.

<span id="SendImageFailed"></span><span id="sendimagefailed"></span><span id="SENDIMAGEFAILED"></span>**SendImageFailed**  
A [SendImageRequest](sendimagerequest.md) message failed to send an image.

<span id="PostScanJobCanceled"></span><span id="postscanjobcanceled"></span><span id="POSTSCANJOBCANCELED"></span>**PostScanJobCanceled**  
A [CancelPostScanJobRequest](cancelpostscanjobrequest.md) message canceled the post-scan job.

<span id="PostScanJobProcessingFailed"></span><span id="postscanjobprocessingfailed"></span><span id="POSTSCANJOBPROCESSINGFAILED"></span>**PostScanJobProcessingFailed**  
The post-scan job failed to run to completion.

<span id="PostScanJobCompletedSuccessfully"></span><span id="postscanjobcompletedsuccessfully"></span><span id="POSTSCANJOBCOMPLETEDSUCCESSFULLY"></span>**PostScanJobCompletedSuccessfully**  
The post-scan job completed successfully.

<span id="PostScanJobCompletedWithErrors"></span><span id="postscanjobcompletedwitherrors"></span><span id="POSTSCANJOBCOMPLETEDWITHERRORS"></span>**PostScanJobCompletedWithErrors**  
The post-scan job completed with errors.

<span id="PostScanJobCompletedWithWarnings"></span><span id="postscanjobcompletedwithwarnings"></span><span id="POSTSCANJOBCOMPLETEDWITHWARNINGS"></span>**PostScanJobCompletedWithWarnings**  
The post-scan job completed with warnings.

 

 





