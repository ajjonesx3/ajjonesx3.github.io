function populate() {

	fetch('./data.json')
		.then(res => res.json())
		.then((data) => {
			let da = data.array;
			for(let i=0;i<da.length;i++){
				let cur_list = da[i][0];
				let entries = da[i][1];
				for(let n=0;n<entries.length;n++){
					let cur_entry = entries[n];
					let left = cur_entry[0];
					let right = cur_entry[1];
					let left_span = document.createElement('span');
					left_span.classList.add("left");
					let right_span = document.createElement('span');
					right_span.classList.add("right");
					let cur_list = document.getElementById(cur_list).value;
					let li = document.createElement('li');
					let dive = document.createElement('div');
					dive.classList.add("entry");
					dive.appendChild(left_span);
					dive.appendChild(right_span);
					li.appendChild(dive);
					cur_list.appendChild(li);
				}
			}
		}).catch(err => console.error(err));

}

window.onload = populate();
