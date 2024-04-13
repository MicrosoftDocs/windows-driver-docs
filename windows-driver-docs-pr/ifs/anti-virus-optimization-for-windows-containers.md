---
title: Anti-virus Optimization for Windows Containers
description: This topic describes optimizations that anti-virus products can utilize when running within Windows Containers.
ms.date: 03/06/2020
---

# Anti-virus optimization for Windows Containers

**The information on this page applies to:**
- Windows 10, versions 1607 and later
- Windows Server 2016 and later versions
- Anti-virus (AV) products running on the Host

This topic describes optimizations that AV products can use to avoid redundant scanning of Windows Container files and help improve Container start up time.

## Container overview

The Windows Container feature is designed to simplify the distribution and deployment of applications. For more information, see the introduction to [Windows Containers](/virtualization/windowscontainers/about/about_overview).

Containers are constructed from any number of package layers. The Windows base OS package forms the first layer.

Each container has an isolated volume that represents the system volume to that container. A container isolation filter (*wcifs.sys*) provides a virtual overlay of package layers onto this container volume. The overlay is achieved using placeholders (reparse points). The volume is seeded with placeholders before the container first accesses the overlain path. Reads of placeholder files are directed to the backing package file. In this way multiple container volumes can access the same underlying package file data stream.

If a container modifies a file, the isolation filter performs copy-on-write and replaces the placeholder with the contents of the package file. This breaks the "linkage" to the package file for that particular container.

## Read redirection

Reads from a placeholder file are redirected to the appropriate package layer by the isolation filter. The redirection is performed at the filter's level. Since the filter is below the AV range, AV filters will not see the read redirection. AV will also not see the opens of package files performed to set up the redirection.

An AV filter does have full view of all operations on the container system volume. It sees operations on placeholder files as well as the file modifications or new file additions.

## Redundant scanning problem

There will likely be many containers depending on the same package layers. The same data stream of a given package file will provide the data for placeholders on multiple container system volumes. As a result, there is potential for redundant AV scans of the same data in every container. This has an unnecessary negative impact on the performance of containers. This is a signification cost given that containers are expected to start quickly and may be short-lived.

## Recommended approach

To avoid redundant scanning on containers it is suggested that an AV product modify its behavior as described below. It is up to the AV product to determine the risk/reward benefit to its customers for this approach. For more about that, see the **Benefits and risks** section at the bottom of this page.

### 1. Package install

During package installation, the management tools will lay out files in the package under the layer root. The AV Filter should continue to scan the files as they are being placed in the package root and it normally would. This ensures that all the files in the layers are initially clean with respect to malware.

### 2. Container start and execution

For real-time scanning of a container volume, AVs should scan in a way that avoids redundancy. Placeholder files need special consideration. Files modified by the container or new files created in the container are not redirected so redundant scanning is not a concern.

To avoid redundant scans, the AV filter first needs to identify container volumes and placeholders on those volumes. For various reasons there is no direct way for an AV filter to query if a volume is a container volume or if a given file is a placeholder file. The isolation filter hides the placeholder reparse point for application compatibility reasons (some applications do not behave correctly if they are aware they are accessing reparse points). Also, a volume is only a container volume while a container is running. The container may be stopped and the volume may remain remounted. Instead, in pre-create, the AV filter must query the file object to determine if it is being opened in the context of a container. It can then attach and ECP to the create and receive the placeholder state on create completion.

The following changes are needed in the AV product:

- **During pre-create on a container volume, attach an ECP to the Create CallbackData that will receive the placeholder information.** These creates can be identified by querying the SILO parameters from the fileobject using **IoGetSiloParameters**. Note the filter must specify the size in the **WCIFS_REDIRECTION_ECP_CONTEXT** structure. All the other fields are out fields set if the ECP is acknowledged.

- **In post-create, if the ECP is acknowledged, examine the ECP redirection flags.** The flags will indicate if the open was serviced from the package layer or from the scratch root (new or modified files). Flags will also indicate if the package layer is registered and whether it is remote.

  - *For opens that are serviced from a remote layer*, AV should skip scanning the file. This is indicated by the redirection flags: `WCIFS_REDIRECTION_FLAGS_CREATE_SERVICED_FROM_LAYER && WCIFS_REDIRECTION_FLAGS_CREATE_SERVICED_FROM_REMOTE_LAYER`

    Remote layers can be assumed to have been scanned on the remote host. Hyper-V Container packages are remote to the utility VM that hosts the container. Those packages will be scanned normally on the Hyper-V host when they are accessed by the utility VM over SMB loop-back.

    Since VolumeGUID and FileId do not apply over remote, these fields will not be set.

  - *For opens that are serviced from a registered layer*, AV should skip scanning the file. This is indicated by the redirection flags: `WCIFS_REDIRECTION_FLAGS_CREATE_SERVICED_FROM_LAYER &&  WCIFS_REDIRECTION_FLAGS_CREATE_SERVICED_FROM_REGISTERED_LAYER`

    The registered layer should be scanned asynchronously during package installation and after signature update.

    >[!NOTE]
    > Registered layers may not be identified by the system in the future. In this case, local layer files must be individually identified as described in the last bullet.

  - *For opens that are serviced from a local package layer*, AV should use the provided VolumeGUID and FileId of the layer file to determine if the file needs to be scanned. This will likely require AV to build a cache of scanned files indexed by volume GUID and FileId. This is indicated by the redirection flag: `WCIFS_REDIRECTION_FLAGS_CREATE_SERVICED_FROM_LAYER`

  - *For new/modified files in the scratch location*, the AV product should scan the files and perform its normal remediation. This is indicated by the redirection flag: `WCIFS_REDIRECTION_FLAGS_CREATE_SERVICED_FROM_SCRATCH`

    Since there is no layer file in this case, VolumeGUID and FileId will not be set.

  - Don't save "this file is serviced from layer" as a permanent marker in its stream context. A file that is initially serviced from the layer root may be modified after the create. In this case, a subsequent create for the same file may indicate that the create is being serviced from the container volume. The AV Filter needs to understand that this can happen.

## Don't use the LayerRootLocations registry key

In the past, we recommended using the `LayerRootLocations` registry key to get the location of base image. AV products should no longer use this registry key. Instead, use the approach recommended in this topic to avoid redundant scanning.

The registry location that had been used to register package layers:

`HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Virtualization\LayerRootLocations`

## Benefits and risks

Consider the following benefits and risks to using these new optimizations for AV products.

### Benefits

- No impact to container start or execution time (even for the first container).
- Avoids scanning of the same content in multiple containers.
- Works for Windows Server Containers. For Hyper-V Container, this works for the packages but requires additional work for running Container.

### Risks

If a container is launched in the time between signature update and the next scheduled proactive anti-malware scan, the files executed in the container are not being scanned with respect to the latest anti-malware signatures. To mitigate this risk, the AV product could skip scans for redirected files only if there has not been a signature update since the last proactive scan. This would limit container performance degradation until a proactive scan is completed with the latest signatures. Optionally, the AV product can trigger a proactive scan in this situation so that subsequent container launches are more efficient.
