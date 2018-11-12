---
title: $ (Alias Interpreter)
description: A dollar sign followed by a pair of braces ( $ ) evaluates to a variety of values related to the specified user-named alias.
ms.assetid: 5182ed99-259e-4e58-8d69-38a702bd8113
keywords: ["$ (Alias Interpreter) Windows Debugging"]
ms.author: domars
ms.date: 09/17/2018
topic_type:
- apiref
api_name:
- $ (Alias Interpreter)
api_type:
- NA
ms.localizationpriority: medium
---

# ${ } (Alias Interpreter)


A dollar sign followed by a pair of braces ( **${ }** ) evaluates to a variety of values related to the specified user-named alias.

```dbgcmd

    Text ${Alias} Text 
    Text ${/d:Alias} Text 
    Text ${/f:Alias} Text 
    Text ${/n:Alias} Text 
    Text ${/v:Alias} Text 
```

## <span id="ddk_token_alias_interpreter_dbg"></span><span id="DDK_TOKEN_ALIAS_INTERPRETER_DBG"></span>Parameters


<span id="Alias"></span><span id="alias"></span><span id="ALIAS"></span>*Alias*  
Specifies the name of the alias to be expanded or evaluated. *Alias* must be a user-named alias or the *Variable* value used by the [**.foreach**](-foreach.md) token.

<span id="_d"></span><span id="_D"></span>**/d**  
Evaluates to one or zero depending on whether the alias is currently defined. If the alias is defined, **${/v:**<em>Alias</em>**}** is replaced by 1; if the alias is not defined, **${/v:**<em>Alias</em>**}** is replaced by 0.

<span id="_f"></span><span id="_F"></span>**/f**  
Evaluates to the alias equivalent if the alias is currently defined. If the alias is defined, **${/f:**<em>Alias</em>**}** is replaced by the alias equivalent; if the alias is not defined, **${/f:**<em>Alias</em>**}** is replaced by an empty string.

<span id="_n"></span><span id="_N"></span>**/n**  
Evaluates to the alias name if the alias is currently defined. If the alias is defined, **${/n:**<em>Alias</em>**}** is replaced by the alias name; if the alias is not defined, **${/n:**<em>Alias</em>**}** is not replaced but retains its literal value of **${/n:**<em>Alias</em>**}**.

<span id="_v"></span><span id="_V"></span>**/v**  
Prevents any alias evaluation. Regardless of whether *Alias* is defined, **${/v:**<em>Alias</em>**}** always retains its literal value of **${/v:**<em>Alias</em>**}**.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For an explanation of how to use aliases, see [Using Aliases](using-aliases.md).

Remarks
-------

If no switches are used and the alias is currently defined, **${**<em>Alias</em>**}** is replaced by the alias equivalent. If no switches are used and the alias is not defined, **${**<em>Alias</em>**}** always retains its literal value of **${**<em>Alias</em>**}**.

One advantage of using the **${ }** token is that the alias will be evaluated even if it is adjacent to other characters. Without this token, the debugger only replaces aliases that are separated from other tokens by a space.

As indicated, there are circumstances where the **${ }** token is not replaced by anything but retains its literal value. This occurs when no switch is used and *Alias* is undefined, when the **/n** switch is used and *Alias* is undefined, and always when the **/v** switch is used. In these circumstances, the token retains its literal value, including the dollar sign and the braces. Therefore, if this is used as the parameter of a command, a syntax error will result, unless that parameter accepts arbitrary text strings.

There is, however, one exception to this. If you use **${/v:**<em>Alias</em>**}** as the first parameter to the [**as (Set Alias)**](as--as--set-alias-.md) or **aS (Set Alias)** command, this token will be treated as the string *Alias* alone, not as the string **${/v:**<em>Alias</em>**}**. This only works with the **as**, **aS**, and **ad** commands, and it only works when the **/v** switch is used—it will not work with **${/n:**<em>Alias</em>**}** or **${**<em>Alias</em>**}** when they retain their literal values.

*Alias* must be a user-named alias or the *Variable* value used by the [**.foreach**](-foreach.md) token—not a fixed-name alias. If there is a fixed-name alias within the string *Alias*, it will be replaced before the **${ }** token is evaluated.

 

 





