---
title: Example 14 Configuring Special Pool
description: Example 14 Configuring Special Pool
ms.assetid: a89f8a08-30e4-4d04-9689-c665b2175780
ms.author: domars
ms.date: 10/12/2018
ms.localizationpriority: medium
---

# Example 14: Configuring Special Pool


Beginning in Windows Vista, you can configure the [Special Pool](special-pool.md) feature as a kernel flag setting or as a registry setting. If you configure it as a kernel flag (run time) setting, you do not need to restart the computer to make the change effective. In earlier versions of Windows, Special Pool is available only as a registry setting.

Also, beginning in Windows Vista, you can set and configure the Special Pool feature from the command line. In earlier versions of Windows, you can set and configure the Special Pool feature only in the Global Flags dialog box.

### <span id="request_special_pool_by_pool_tag_without_rebooting"></span><span id="REQUEST_SPECIAL_POOL_BY_POOL_TAG_WITHOUT_REBOOTING"></span>Request Special Pool by pool tag without rebooting

The following command requests special pool for all allocations with the **Tag1** pool tag. This setting becomes effective immediately, but it is lost if you shut down or restart Windows.

This command uses the **/k** parameter to specify a kernel flag (run time) setting and the +spp abbreviation to set a special pool request.

```console
gflags /k +spp Tag1
```

Gflags responds by printing:

```console
Special Pool set to 0x31676154
PoolTagOverruns set to 0x1
Current Running Kernel Settings are: 00000000
```

Notice that the special pool allocation request is not a kernel flag setting and is not reflected in the kernel settings value.

Also, a special pool allocation request does not change the value of the overrun (0x1) or underrun (0x0) setting for special pool. To change from overruns, the default, to underruns, use the Gflags Dialog Box. For information, see [Detecting Overruns and Underruns](detecting-overruns-and-underruns.md).

You cannot display the pool tag at the command line. To verify that the pool tag is a kernel setting, use the Gflags Dialog Box.

### <span id="request_special_pool_by_pool_tag_in_the_registry"></span><span id="REQUEST_SPECIAL_POOL_BY_POOL_TAG_IN_THE_REGISTRY"></span>Request Special Pool by pool tag in the registry

The following command requests special pool for all allocations with the **Tag1** pool tag. Because this setting is stored in the registry, you must restart the computer to make it effective, but it remains effective until you change it.

This command uses the **/r** parameter to specify a registry setting and the +spp abbreviation to set a special pool request.

```console
gflags /r +spp Tag1
```

Gflags responds by printing:

```console
Special Pool set to 0x31676154
PoolTagOverruns set to 0x1
Current Boot Registry Settings are: 00000000
```

Notice that the special pool allocation request is not a registry flag setting and is not reflected in the registry settings value.

Also, a special pool allocation request does not change the value of the overrun (0x1) or underrun (0x0) setting for special pool. To change from overruns, the default, to underruns, use the Gflags Dialog Box. For information, see [Detecting Overruns and Underruns](detecting-overruns-and-underruns.md).

To verify that the value has been added to the registry, use Reg or Regedit to display the value of the **PoolTag** entry in the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management** key.

For example:

```console
c:>reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" -v PoolTag
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management
    PoolTag    REG_DWORD    0x31676154
```

### <span id="request_special_pool_by_size_without_rebooting"></span><span id="REQUEST_SPECIAL_POOL_BY_SIZE_WITHOUT_REBOOTING"></span>Request Special Pool by size without rebooting

The following command requests special pool for allocations of 1 to 8 bytes on an x86 computer with a PAGE\_SIZE of 0x1000 and allocation granularity of 8 bytes.

This command uses the **/k** parameter to specify a kernel flag (run time) setting and the +spp abbreviation to set a special pool request. The size value is preceded by 0x to indicate that it is a size and not a pool tag.

The value, 0x10, is calculated by adding the allocation granularity (8 bytes) to the largest size in the range (8 bytes) for a total of 16 bytes (0x10). For help in determining the correct value to enter, see "Selecting an Allocation Size" in [Special Pool](special-pool.md).

```console
gflags /k +spp 0x10
```

Gflags responds by printing:

```console
Special Pool set to 0x10
PoolTagOverruns set to 0x1
Current Running Kernel Settings are: 00000000
```

Again, the special pool allocation request is not a kernel flag setting and is not reflected in the kernel settings value.

Also, a special pool allocation request does not change the value of the overrun (0x1) or underrun (0x0) setting for special pool. To change from overruns, the default, to underruns, use the Gflags Dialog Box. For information, see [Detecting Overruns and Underruns](detecting-overruns-and-underruns.md).

### <span id="request_special_pool_by_size_in_the_registry"></span><span id="REQUEST_SPECIAL_POOL_BY_SIZE_IN_THE_REGISTRY"></span>Request Special Pool by size in the registry

The following command requests special pool for allocations of 1024 to 1040 bytes on an x64 computer with a PAGE\_SIZE of 0x1000 and allocation granularity of 16 bytes.

This command uses the **/r** parameter to specify a system-wide registry setting and the +spp abbreviation to set a special pool request. The size value is preceded by 0x to indicate that it is a size and not a pool tag.

The value, 0x420, is calculated by adding the allocation granularity (16 bytes) to the largest size in the range (1040 bytes) for a total of 1056 bytes (0x420). For help in determining the correct value to enter, see "Selecting an Allocation Size" in [Special Pool](special-pool.md).

```console
gflags /r +spp 0x420
```

Gflags responds by printing:

```console
Special Pool set to 0x420
PoolTagOverruns set to 0x1
Current Boot Registry Settings are: 00000000
```

Again, the special pool allocation request is not a registry flag setting and is not reflected in the registry settings value.

Also, a special pool allocation request does not change the value of the overrun (0x1) or underrun (0x0) setting for special pool. To change from overruns, the default, to underruns, use the Gflags Dialog Box. For information, see [Detecting Overruns and Underruns](detecting-overruns-and-underruns.md).

To verify that the value has been added to the registry, use Reg or Regedit to display the value of the **PoolTag** entry in the **HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management** key.

For example:

```console
c:>reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management" -v PoolTag
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management
    PoolTag    REG_DWORD    0x420
```

### <span id="cancel_a_special_pool_request"></span><span id="CANCEL_A_SPECIAL_POOL_REQUEST"></span>Cancel a Special Pool Request

The following command cancels a request for Special Pool as a kernel flag (run time) setting. The command is the same for a request by pool tag or by size.

```console
gflags /k -spp
```

The following command cancels a request for Special Pool as a registry setting. The command is the same for a request by pool tag or by size.

```console
gflags /r -spp
```

When the command is successful, Gflags responds by printing:

```console
Special Pool value has been deleted.
```

 

 





