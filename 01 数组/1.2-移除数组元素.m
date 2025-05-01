nums = input('请输入数组元素，套中括号并用空格分隔：');
val = input('请输入要删除的元素：');

% 直接删除指定元素
newNums = nums(nums ~= val);
newLength = length(newNums);

% 输出结果
fprintf('删除元素后的数组为');
disp(newNums);
fprintf('数组长度为%d\n', newLength);