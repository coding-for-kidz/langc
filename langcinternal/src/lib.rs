use std::collections::HashMap;
use std::fs::metadata;
use walkdir::WalkDir;
use log::{debug};

pub fn get_percents(to_get: &HashMap<String, i32>) -> HashMap<&str, f32> {
    debug!("get_percents");
    let mut to_return: HashMap<&str, f32> = HashMap::new();
    let mut total_sum: i32 = 0;
    for (_key, value) in &*to_get {
        total_sum += value;
    }
    for (key, value) in &*to_get {
        let percent = (*value as f32 / total_sum as f32) * 100.0;
        let reduced_percent: f32 = percent - (percent % 0.01);
        to_return.insert(key, reduced_percent);
    }
    return to_return;
}


pub fn should_ignore(ignore_dirs: &[String], path_str: &str) -> bool {
    debug!("should_ignore");
    let md = metadata(path_str).unwrap();
    if md.is_dir() {
        return true;
    }
    let path_list: Vec<&str> = path_str.split("\\").collect();
    for item in ignore_dirs {
        let item_str: &str = &item[..];
        if path_list.contains(&item_str) {
            return true;
        }
    }
    return false;
}

pub fn get_all(ignore: Vec<String>, ignore_file_ext: Vec<String>) -> Vec<String> {
    debug!("get_all");
    let mut all_files_list: Vec<String> = Vec::new();
    for directory in WalkDir::new("..").into_iter().filter_map(|e| e.ok()) {
        let ignore_item: bool = should_ignore(&ignore, directory.path().to_str().unwrap());
        if !ignore_item {
            let mut go: bool = true;
            for ending in &ignore_file_ext {
                if directory.file_name().to_str().unwrap().ends_with(&ending[..]) {
                    go = false;
                }
            }
            if go {
                all_files_list.push(directory.file_name().to_str().unwrap().to_string());
            }
        }
    }
    return all_files_list;
}


pub fn find_langs() -> HashMap<String, i32> {
    debug!("find_langs");
    let mut langs: HashMap<String, i32> = HashMap::new();
    let ignore = vec!["venv".to_string(), "node_modules".to_string(), ".git".to_string(),
                      ".idea".to_string(), ".vs".to_string(), "target".to_string(),
                      ".pytest_cache".to_string()];
    let ignore_file_ext = vec![".gitignore".to_string(), ".gitmodules".to_string(),
                               ".webmanifest".to_string(), ".png".to_string(), ".jpg".to_string(),
                               ".name".to_string(), ".pyc".to_string(), ".http".to_string(),
                               ".TAG".to_string(), "DS_Store".to_string(), ".gz".to_string(),
                               ".PNG".to_string(), "lastfailed".to_string(), "nodeids".to_string(),
                               "git".to_string(), "stepwise".to_string(), "Procfile".to_string(),
                               "sqlite".to_string(), "db".to_string(), "LICENSE".to_string(),
                               "list".to_string(), ".ico".to_string(), ".svg".to_string(),
                               ".map".to_string(), ".xcf".to_string(), ".cfg".to_string(),
                               ".txt".to_string(), ".json".to_string(), ".conf".to_string(),
                               ".xml".to_string(), ".ini".to_string(), ".types".to_string(),
                               ".yml".to_string(), ".in".to_string(), "Makefile".to_string(),
                               ".lock".to_string(), ".toml".to_string()];
    let all_files = get_all(ignore, ignore_file_ext);
    for file in all_files {
        let mut dotsplit: Vec<&str> = file.split(".").collect();
        if let Some(ending_some) = dotsplit.pop() {
            let ending = ending_some.to_string();
            if langs.contains_key(&ending) {
                *langs.get_mut(&ending).unwrap() += 1;
            } else {
                langs.insert(ending, 1);
            }
        }
    }
    return langs;
}