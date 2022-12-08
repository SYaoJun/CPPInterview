fn plus(x: i32, y: i32) -> i32 {
    x + y
}

fn main() {
    let x = 10;
    let y = 20;
    println!("{} + {} = {}", x, y, plus(x, y))
}

#[test]
fn it_works() {
    assert_eq!(4, plus(2, 2), );
}