---
title: Filtering Registry Operations on Application Hives
description: Initial support for application hives was introduced in Windows Vista.
ms.date: 11/04/2021
ms.custom: contperf-fy22q2
---

# Filtering Registry Operations on Application Hives

User-mode applications use [application hives in the registry](/windows/win32/sysinfo/registry-hives) to store app-specific state data.

A registry filter driver receives calls to its [*RegistryCallback*](/windows-hardware/drivers/ddi/wdm/nc-wdm-ex_callback_function) routine for registry operations on application hives.
These calls do not distinguish between registry operations on application hives and operations on other types of registry hives.

To load an application hive, an app calls [**RegLoadAppKey**](/windows/win32/api/winreg/nf-winreg-regloadappkeya).

Application hives are loaded under `\\REGISTRY\\A` instead of under `\\REGISTRY\\MACHINE` or `\\REGISTRY\\USER`.

Note that there is no way to traverse `\\REGISTRY\\A`. An attempt to open a key under \\REGISTRY\\A fails with error status **STATUS_ACCESS_DENIED**.

To access a key in an application hive, an app uses the handle that it receives when it calls **RegLoadAppKey**.

The operating system automatically unloads the application hive after all of the handles to the hive are closed.

In contrast to other types of registry hives, for which each key is secured with its own security descriptor, the security of an application hive is based on the hive file's security descriptor.
This means that:

* An attempt to set a security descriptor on an individual key in an application hive fails with error status **STATUS_ACCESS_DENIED**.
* An entity that is successful in loading the hive can modify the entire hive.

Registry filter drivers that handle create-key and open-key operations (which are indicated by the **RegNtPreOpenKey**, **RegNtPreOpenKeyEx**, **RegNtPreCreateKey**, and **RegNtPreCreateKeyEx** notification values) must
 take care not to use an absolute path (one starting with `\\REGISTRY\\A\\`) to open an application hive; only the registry manager can do this.
If a registry filter driver tries to open an application hive in this way (for example, by calling the [**ZwOpenKey**](/windows-hardware/drivers/ddi/wdm/nf-wdm-zwopenkey) routine), the operation fails with
 error status **STATUS_ACCESS_DENIED**.

The absolute path name string appears in the **CompleteName** member of the
 [**REG_CREATE_KEY_INFORMATION**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_reg_create_key_information), [**REG_CREATE_KEY_INFORMATION_V1**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_reg_create_key_information_v1),
 **REG_OPEN_KEY_INFORMATION**, or **REG_OPEN_KEY_INFORMATION_V1** structure.
