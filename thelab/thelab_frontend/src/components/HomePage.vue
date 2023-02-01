<template>
	<div class="homepage">
		<div class="columns is-multiline">
			<div class="column">
				<figure class="image is-3by1">
					<img alt="Vue logo" src="../assets/logo.png" />
				</figure>
			</div>
		</div>

		<div class="columns is-centered">
			<div
				v-for="(card, index) in card_list"
				:key="index"
				class="column is-3 is-offset-one-tenth"
			>
				<div class="card">
					<div class="card-image">
						<figure class="image is-128by128">
							<img
								src="https://bulma.io/images/placeholders/1280x960.png"
								alt="Placeholder image"
							/>
						</figure>
					</div>
					<div class="card-content">
						<div class="content">
							Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus
							nec iaculis mauris. <a>@bulmaio</a>. <a href="#">#css</a>
							<a href="#">#responsive</a>
							<br />
						</div>
					</div>
				</div>
			</div>
		</div>

		<div class="columns is-centered">
			<div class="column is-10 main-content">
				{{ main_content }}
			</div>
		</div>

		<div class="columns is-centered">
			<div class="column is-1">
				<button class="button is-info">Contact</button>
			</div>

			<div class="column is-8"></div>

			<div class="column is-1">
				<span class="icon-text">
					<span class="icon">
						<i class="fab fa-facebook-f"></i>
					</span>
				</span>
				<span class="icon-text">
					<span class="icon">
						<i class="fab fa-twitter"></i>
					</span>
				</span>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: "HomePage",
		data() {
			return {
				card_list: [
					{
						id: 0,
						msg: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris.",
					},
					{
						id: 1,
						msg: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris.",
					},
					{
						id: 2,
						msg: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus nec iaculis mauris.",
					},
				],
				main_content:
					"Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
					          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
					          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
					          nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \
					          in reprehenderit in voluptate velit esse cillum dolore eu fugiat \
					          nulla pariatur. Excepteur sint occaecat cupidatat non proident, \
					          sunt in culpa qui officia deserunt mollit anim id est laborum. \
					          Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
					          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
					          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
					          nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \
					          in reprehenderit in voluptate velit esse cillum dolore eu fugiat \
					          nulla pariatur. Excepteur sint occaecat cupidatat non proident, \
					          sunt in culpa qui officia deserunt mollit anim id est laborum. \
					          Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
					          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
					          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
					          nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \
					          in reprehenderit in voluptate velit esse cillum dolore eu fugiat \
					          nulla pariatur. Excepteur sint occaecat cupidatat non proident, \
					          sunt in culpa qui officia deserunt mollit anim id est laborum. \
					          Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
					          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
					          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
					          nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \
					          in reprehenderit in voluptate velit esse cillum dolore eu fugiat \
					          nulla pariatur. Excepteur sint occaecat cupidatat non proident, \
					          sunt in culpa qui officia deserunt mollit anim id est laborum. \
					          Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
					          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
					          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
					          nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \
					          in reprehenderit in voluptate velit esse cillum dolore eu fugiat \
					          nulla pariatur. Excepteur sint occaecat cupidatat non proident, \
					          sunt in culpa qui officia deserunt mollit anim id est laborum. \
					          Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
					          sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. \
					          Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris \
					          nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor \
					          in reprehenderit in voluptate velit esse cillum dolore eu fugiat \
					          nulla pariatur. Excepteur sint occaecat cupidatat non proident, \
					          sunt in culpa qui officia deserunt mollit anim id est laborum.",
			};
		},
	};
</script>

<style scoped lang="scss">
	h3 {
		margin: 40px 0 0;
	}
	ul {
		list-style-type: none;
		padding: 0;
	}
	li {
		display: inline-block;
		margin: 0 10px;
	}
	a {
		color: #42b983;
	}

	.main-content {
		font-family: "Roboto", sans-serif;
		font-size: larger;
	}
</style>
