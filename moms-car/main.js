function populate() {

	fetch('./data.json')
		.then(res => res.json())
		.then((data) => {
			let da = data.array;
			for(let i=0;i<da.length;i++){
				let left = da[i][0];
				let right = da[i][1];
				console.log(left);
				//make list items out of left and right
			}
		}).catch(err => console.error(err));

}

window.onload = populate();
