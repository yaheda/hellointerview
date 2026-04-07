pub fn solution() {
    println!("two_sums");
    let nums = [1,3,4,6,8,10,13];
    let res = is_pair_sum(&nums, 6);
    println!("{}", res);

}

fn is_pair_sum(nums: &[i32], target: i32) -> bool {
    let mut left = 0;
    let mut right = (nums.len() as i32) - 1;

    while left < right {
        let condition = nums[left as usize] + nums[right as usize];
        println!("{}", condition);
        if condition == target {
            return true;
        }

        if condition < target {
            left += 1;
        } else {
            right -= 1;
        }
    }

    return false;
}