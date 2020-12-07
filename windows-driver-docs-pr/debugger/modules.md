---
title: Modules
description: Modules
keywords: ["symbols, modules", "modules"]
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Modules


## <span id="modules"></span><span id="MODULES"></span>


An *image* is an executable, DLL, or driver that Windows has loaded as part of a user-mode process or the kernel. The file from which the image was loaded is referred to as its *image file*.

The [debugger engine](introduction.md#debugger-engine) caches a list of *modules* for each process (or, in kernel-mode, the virtual process). Typically each module in this list represents an image in the process. The engine's module list can be synchronized with the target using **Reload**.

**Note**   In kernel-mode debugging, the engine's module list for the virtual process contains both the system-wide kernel-mode modules and the current process's user-mode modules.

 

A module can be specified by its base address in the target's virtual address space, or by its index in the list of modules the engine maintains for the target. The module's index equals its position in the list of modules, and therefore this index will change if a module with a lower index is unloaded. All unloaded modules have indexes; these are always higher than the indexes of loaded modules. The base address of a module will not change as long as it remains loaded; in some cases it may change if the module is unloaded and then reloaded.

The index is a number between zero and the number of modules in the target minus one. The number of modules in the current process can be found by calling [**GetNumberModules**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getnumbermodules).

The index can be used to find the base address by calling [**GetModuleByIndex**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getmodulebyindex). The base address of a module owning a symbol with a given name can be found using [**GetSymbolModule**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getsymbolmodule).

The following methods return both the index and base address of the specified module:

-   To find a module with a given module name, use [**GetModuleByModuleName**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getmodulebymodulename).

-   The module whose virtual address range contains a given address is returned by [**GetModuleByOffset**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getmodulebyoffset). This method can be used to find the module index given the base address of the module.

The following methods return information about modules specified either by base address or index:

-   The names of a module are returned by [**GetModuleNames**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getmodulenames) and [**GetModuleNameString**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getmodulenamestring).

-   Version information for the module is returned by [**GetModuleVersionInformation**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getmoduleversioninformation).

-   Some of the parameters used to describe a module are returned by [**GetModuleParameters**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getmoduleparameters). For details on the parameters returned by this method, see [**DEBUG\_MODULE\_PARAMETERS**](/windows-hardware/drivers/ddi/dbgeng/ns-dbgeng-_debug_module_parameters).

### <span id="unloaded_modules"></span><span id="UNLOADED_MODULES"></span>Unloaded Modules

During user-mode debugging, unloaded modules are tracked only in Windows Server 2003 and later versions of Windows. Earlier versions of Windows only tracked unloaded modules in kernel mode. When they are tracked, they are indexed after the loaded modules. Hence any method that searches the target's modules will search all the loaded modules and then the unloaded modules. Unloaded modules can be used to analyze failures caused by an attempt to call unloaded code.

### <span id="synthetic_modules"></span><span id="SYNTHETIC_MODULES"></span> Synthetic Modules

*Synthetic modules* can be created as a way to label a region of memory. These modules cannot contain real symbols, but they can contain synthetic symbols. The method [**AddSyntheticModule**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-addsyntheticmodule) creates a new synthetic module. Synthetic modules can be removed using [**RemoveSyntheticModule**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-removesyntheticmodule). Reloading all the modules in the target deletes all synthetic modules.

### <span id="image_path"></span><span id="IMAGE_PATH"></span>Image Path

The *executable image path* is used by the engine when searching for executable images.

The executable image path can consist of several directories separated by semicolons (**;**). These directories are searched in order.

For an overview of the executable image path, see Executable Image Path.

To add a directory to the executable image path, use the method [**AppendImagePath**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-appendimagepath). The whole executable image path is returned by [**GetImagePath**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-getimagepath) and can be changed using [**SetImagePath**](/windows-hardware/drivers/ddi/dbgeng/nf-dbgeng-idebugsymbols3-setimagepath).

### <span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about processes and virtual processes, see [Threads and Processes](controlling-threads-and-processes.md).

 

