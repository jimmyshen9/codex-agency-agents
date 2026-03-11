# 调试工作流模板

适用于：线上问题复现、接口异常、任务失败、状态不一致、性能抖动。

把下面这段作为提示词交给 Codex：

```text
使用 engineering-codex-implementation 先定位问题，必要时再切换 engineering-codex-security-review 或 engineering-codex-incident-response。

输出顺序固定为：
1. [现象]
2. [假设]
3. [验证]
4. [结论]
5. [修复]
6. [回归检查]

要求：
- 不要一次性铺开太多猜测。
- 每次优先验证最可能的 1 到 2 个假设。
- 如果需要改代码，先解释为什么改。
- 所有调试说明优先中文。
- 不使用 emoji。
```
