function populate() {

	fetch('.data/data.json')
		.then(res => res.json())
		.then((data) => {
			let da = data.array;
			for(let i=0;i<da.length;i++){
				var cur_list = da[i][0];
				var entries = da[i][1];
				for(let n=0;n<entries.length;n++){
					let cur_entry = entries[n];
					let left = cur_entry[0];
					let right = cur_entry[1];

					if(right == "-1"){
						right = "N/A"
					}

					let left_span = document.createElement('span');
					left_span.classList.add("left");
					left_link = document.createElement('a');
					left_link.textContent = left;

					let car_name = left.split(" ");
					left_link.href="https://cars.usnews.com/cars-trucks/" + car_name[0].toLowerCase() + "/" + car_name[1].toLowerCase()
					left_link.target = "__blank";

					left_span.appendChild(left_link);

					let right_span = document.createElement('span');
					right_span.classList.add("right");
					right_span.textContent = right;

					let cur_ol = document.getElementById(cur_list);
					let li = document.createElement('li');
					let dive = document.createElement('div');
					dive.classList.add("entry");
					dive.appendChild(left_span);
					dive.appendChild(right_span);
					li.appendChild(dive);
					cur_ol.appendChild(li);
				}
			}
		}).catch(err => console.error(err));

}

window.onload = populate();
