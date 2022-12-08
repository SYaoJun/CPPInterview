/***
fn input()->i32{
    let mut index = String::new();
    use std::io;
    // 读一行
    io::stdin().read_line(&mut index).expect("not a num");
    let mut res = 0;
    let trimmed = index.trim();
    match trimmed.parse::<i32>() {
        Ok(num) => res = num,
        Err(..) => println!("this was not an integer: {}", trimmed),
    }
    res
}
fn main() {
    #[warn(unused_assignments)]
    let mut t: i32 = 0;
    t = input();
     for j in 0..t {
         let mut array: [i32; 3]=[0,0,0];
         for i in 0..3{
             array[i] = input();
         }
         array.sort();
         println!("{}", array[1]);
     }
}
*/

fn main() {
    let mut test_cases = String::new();
    std::io::stdin().read_line(&mut test_cases).unwrap();
    let t: i32 = test_cases.trim().parse().unwrap();
    for _ in 0..t {
        let mut input_string = String::new();
        std::io::stdin().read_line(&mut input_string).unwrap();
        let mut numbers: Vec<u16> = input_string.split(" ").map(|x| x.trim().parse::<u16>().unwrap()).collect();
        numbers.sort();
        println!("{}", numbers[1]);
    }
}
