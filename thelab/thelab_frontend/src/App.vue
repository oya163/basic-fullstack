<template>
	<div id="wrapper">
		<!-- Navigation bar section -->
		<nav
			class="navbar is-fixed-top is-transparent"
			role="navigation"
			aria-label="dropdown navigation"
		>
			<div class="navbar-brand has-navbar-fixed-top">
				<router-link to="/" class="navbar-item">
					<img src="./assets/logo.gif" width="112" height="128" />
					<h1 class="company-name">{{ companyName }}</h1>
				</router-link>
			</div>

			<div
				class="navbar-menu has-navbar-fixed-top has-text-centered"
				id="navbar-menu"
			>
				<div class="navbar-start"></div>

				<div class="navbar-end is-spaced">
					<div class="navbar-item">
						<router-link
							to="/"
							class="navbar-item has-text-weight-medium summary navbar-text"
						>
							Home
						</router-link>
					</div>

					<div class="navbar-item">
						<router-link
							to="/products"
							class="navbar-item has-text-weight-medium summary navbar-text"
						>
							Products
						</router-link>
					</div>

					<div class="navbar-item">
						<router-link
							to="/company"
							class="navbar-item has-text-weight-medium summary navbar-text"
						>
							Company
						</router-link>
					</div>

					<div class="navbar-item">
						<router-link
							to="/blog"
							class="navbar-item has-text-weight-medium summary"
						>
							Blog
						</router-link>
					</div>
				</div>
			</div>
		</nav>

		<!-- Main content section -->
		<section class="section mt-5">
			<router-view />
		</section>

		<!-- Footer section -->
		<footer class="footer">
			<p class="has-text-centered">Copyright (c) 2023</p>
		</footer>
	</div>
</template>

<script>
	import axios from "axios";

	export default {
		data() {
			return {
				companyName: "thelab",
			};
		},
		mounted() {
			this.getCompanyName();
		},
		methods: {
			getCompanyName() {
				axios
					.get(`/api/companyname/`)
					.then((response) => {
						this.companyName = response.data.name;
						document.title = this.companyName;
						return response.data.name;
					})
					.catch((error) => {
						console.log(error);
					});
			},
		},
	};
</script>

<style lang="scss">
	$navbar-height: 10rem;

	@import "../node_modules/bulma";

	.company-name {
		font-family: "Lobster Two";
		font-size: 7rem;
	}

	.navbar-text {
		border-right: 1px solid gray;
	}

	.navbar-item img {
		max-height: 7rem;
	}

	.footer {
		padding-top: 10rem;
	}
</style>
