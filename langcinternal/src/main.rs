mod lib;

use log::{info};


fn main() {
    info!("start");
    let nums = lib::find_langs();
    let p = lib::get_percents(&nums);
    for (_key, value) in &p {
        println!("{value}");
    }
    println!("");
    for (key, _value) in &p {
        println!("{key}");
    }
}